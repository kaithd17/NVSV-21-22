const ws = new WebSocket("ws://127.0.0.1:5678/");

const getUsername = () => {
  return document.getElementById("displayUsername").innerText.split(": ")[1];
};

const setUserCount = () => {
  document.getElementById("onlineStatus").innerHTML =
    "User" + (data.count == 1 ? "" : "s") + " Online: " + data.count;
};

const setValidUsername = () => {
  let username = document.getElementById("username").value;
  if (username !== "") {
    document.getElementById("displayUsername").innerHTML =
      "Username: " + username;
    document.getElementById("username").style.display = "none";
    document.getElementById("userButton").style.display = "none";
    return true;
  }
  return false;
};

const registerUser = () => {
  if (setValidUsername()) {
    ws.send(JSON.stringify({ action: "newUser", username: getUsername() }));
    document.getElementById("sendButton").disabled = false;
  }
};

const showMessage = (data) => {
  if (data.message != undefined && data.username != undefined) {
    let username = getUsername();
    let template;
    let node;
    if (username === data.username) {
      template = document.getElementById("messageTemplate");
      node = template.content.cloneNode(true);
      node.getElementById("user").innerHTML = "You: ";
    } else {
      template = document.getElementById("messageTemplate2");
      node = template.content.cloneNode(true);
      node.getElementById("user").innerHTML = data.username + ": ";
    }
    node.getElementById("messageText").innerHTML = data.message + "";
    document.getElementById("messages").appendChild(node);
  }
};

const showInfoMessage = (data, action) => {
  let template = document.getElementById("infoTemplate");
  let node = template.content.cloneNode(true);
  if (action === "addUser") {
    node.getElementById("messageContainer2").style.backgroundColor = "#00b8f5";
    node.getElementById("messageText").innerHTML =
      data.username + " joined the chat.";
  } else {
    node.getElementById("messageContainer2").style.backgroundColor = "#d33030";
    node.getElementById("messageText").innerHTML =
      data.username + " left the chat.";
  }
  document.getElementById("messages").appendChild(node);
};

const sendMessage = () => {
  document.getElementById("message").innerHTML = "";
  let username = getUsername();
  let message = document.getElementById("message").value;
  if (message !== "") {
    ws.send(
      JSON.stringify({
        action: "newMessage",
        username: username,
        message: message,
      })
    );
    document.getElementById("message").value = "";
  }
};

ws.onmessage = (e) => {
  data = JSON.parse(e.data);
  switch (data.type) {
    case "users":
      setUserCount();
      showInfoMessage(data, data.action);
    case "message":
      showMessage(data);
  }
};
