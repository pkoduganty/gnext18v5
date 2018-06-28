
const admin = require('firebase-admin');
const functions = require('firebase-functions');
const underscore = require('underscore');

admin.initializeApp();
const db = admin.firestore();

/** Collections and fields names in Firestore */
const FirestoreNames = {
  NOTICE_BOARD: "notice-board",
  USERS: 'students',
  USER_ID: 'googleId',
  INTENT: 'push_intent',
};

const DialogFlowNames = {
  LATEST_NEWS_INTENT: 'push_notification_news_intent'
};

exports.createAnnouncementTrigger = functions.firestore
  .document(`${FirestoreNames.NOTICE_BOARD}/{noticeId}`)
  .onCreate((snap, context) => {
	const record = snap.data();
    const request = require('request');
    const google = require('googleapis');
    const serviceAccount = require('./service-account.json');
    const jwtClient = new google.auth.JWT(
      serviceAccount.client_email, null, serviceAccount.private_key,
      ['https://www.googleapis.com/auth/actions.fulfillment.conversation'],
      null
    );
    let notification = {
      userNotification: {
        title: record.title,
        description: record.text,
        school: record.school,
        grade: record.grade,
        course: record.class,
        category: record.category,
        createDate: record.createdDate,
        validTillDate: record.validTillDate
      },
      target: {},
    };
    jwtClient.authorize((err, tokens) => {
      if (err) {
        throw new Error(`Auth error: ${err}`);
      }
      db.collection(FirestoreNames.USERS)
        .where(FirestoreNames.INTENT, '==', DialogFlowNames.LATEST_NEWS_INTENT)
        .get()
        .then((querySnapshot) => {
          querySnapshot.forEach((user) => {
            notification.target = {
              userId: user.get(FirestoreNames.USER_ID),
              intent: user.get(FirestoreNames.INTENT)
            };
            request.post('https://actions.googleapis.com/v2/conversations:send', {
              'auth': {
                'bearer': tokens.access_token,
              },
              'json': true,
              'body': {'customPushMessage': notification, 'isInSandbox': true},
            }, (err, httpResponse, body) => {
              if (err) {
                throw new Error(`API request error: ${err}`);
              }
              console.log(`${httpResponse.statusCode}: ` +
                `${httpResponse.statusMessage}`);
              console.log(JSON.stringify(body));
            });
          });
        })
        .catch((error) => {
          throw new Error(`Firestore query error: ${error}`);
        });
    });
    return 0;
  });

// Use this function to restore the content of the students database.
exports.restoreStudentsData = functions.https.onRequest((request, response) => {
  db.collection(FirestoreNames.USERS)
    .get()
    .then((querySnapshot) => {
      if (querySnapshot.size > 0) {
        let batch = db.batch();
        querySnapshot.forEach((doc) => {
          batch.delete(doc.ref);
        });
        batch.commit()
          .then(addTips);
      }
    })
    .catch((error) => {
      throw new Error(`Firestore query error: ${error}`);
    });
  addStudents();

  function addStudents() {
    const students = require('./students.json');
    let batch = db.batch();
    let dbRef = db.collection(FirestoreNames.USERS);
    students.forEach((s) => {
      let sRef = dbRef.doc();
      batch.set(sRef, s);
    });
    batch.commit()
      .then(() => {
        response.send(`Students Data succesfully restored`);
      })
      .catch((error) => {
        throw new Error(`Error restoring students data: ${error}`);
      });
  }
});


// Use this function to add new notifications to the notice-board database.
exports.createNotice = functions.https.onRequest((data, context) => {
	const sample_notifications = require('./notifications.json');
	var addDoc = db.collection(FirestoreNames.NOTICE_BOARD).add(underscore.sample(sample_notifications)).then(ref => {
	  console.log('Added notification with ID: ', ref.id);
	});
});
