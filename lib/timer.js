let state = false;

const countdown = () => {
  // if ()
  sendMessage();
};

const sendMessage = () => {
  console.log("message sent");
};

const main = () => {
  console.log("starting");
  if (!state) {
    setTimeout(() => {
      console.log("time up!");
      if (!state) {
        sendMessage();
      } else {
        console.log("cancelled timer");
      }
    }, 5 * 1000);
  }
  // state = true;
};

main();

// var isMomHappy = false;

// Promise
// var willIGetNewPhone = new Promise(function(resolve, reject) {
//   if (isMomHappy) {
//     var phone = {
//       brand: "Samsung",
//       color: "black"
//     };
//     resolve(phone); // fulfilled
//   } else {
//     var reason = new Error("mom is not happy");
//     reject(reason); // reject
//   }
// });

// var showOff = function(phone) {
//   var message =
//     "Hey friend, I have a new " + phone.color + " " + phone.brand + " phone";

//   return Promise.resolve(message);
// };

// var askMom = function() {
//   console.log("before asking Mom"); // log before
//   willIGetNewPhone
//     .then(showOff)
//     .then(function(fulfilled) {
//       console.log(fulfilled);
//     })
//     .catch(function(error) {
//       console.log(error.message);
//     });
//   console.log("after asking mom"); // log after
// };

// askMom();
