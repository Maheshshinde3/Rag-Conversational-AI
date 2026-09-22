// ===============================
// Opens document section
// ===============================

const knowledgeBtn = document.getElementById("knowledgeBtn");  // Get the Knowledge Base button
const kbPanel = document.getElementById("kbPanel");    // Get the Knowledge Base / Upload Documents section
const conversation = document.getElementById("conversation");

// When Knowledge Base is clicked
knowledgeBtn.addEventListener("click", function () {
  // Open the upload documents section
  kbPanel.classList.add("open");
  knowledgeBtn.classList.add("active");
  conversation.classList.remove("active");

});

// close document upload section
const Documentclose = document.getElementById("closeKb");
Documentclose.addEventListener("click", function () {
  // Open the upload documents section
  kbPanel.classList.remove("open");
  knowledgeBtn.classList.remove("active");
  conversation.classList.add("active");
});










// ===============================
// adding documents
// ===============================

const uploadZone = document.getElementById("uploadZone");
const fileInput = document.getElementById("fileInput");

uploadZone.addEventListener("click", function () {
  fileInput.click();
});

//sending file to backend
fileInput.addEventListener("change", async () => {
  const file = fileInput.files[0];

  // Check if file is PDF
  if (file.type !== "application/pdf") {
    alert("Only PDF files are allowed");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch("http://127.0.0.1:8000/upload", {
    method: "POST",
    body: formData,
  });

  const data = await response.json();

  alert(data.message);
});











// ===============================
//All about giving query and sending it to llm
// ===============================

const sendbtn = document.getElementById("sendBtn");
const message = document.getElementById("messageInput");

sendbtn.addEventListener("click", async function () {
  sendbtn.classList.add("enabled");
  
  query = message.value;
  const response = await fetch("http://127.0.0.1:8000/query", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      query: query,
    }),
  });











 // ===============================
 //Printing Received Answer from llm
 // ===============================

  const data = await response.json();

  if (data.number === 0) {
    alert(data.errors);
  } 
  else {
    document.getElementById("hero").style.display = "none";
    // Get the chat area from HTML
    const chatArea = document.getElementById("chatArea");

    const userMessage = document.createElement("div");
    // Give the div two CSS classes
    userMessage.classList.add("message", "user");

    // Put the user's question inside the div
    userMessage.textContent = data.query;

    // Put this div inside the chat area
    chatArea.appendChild(userMessage);

  

    // Add AI message
   

    // Create another new div
    const aiMessage = document.createElement("div");

    // Give the div two CSS classes
    aiMessage.classList.add("message", "ai");

    // Put the AI's answer inside the div
    aiMessage.textContent = data.answer;

    // Put this div inside the chat area
    chatArea.appendChild(aiMessage);
    console.log(data.query)
    console.log(data.answer)
 }

sendbtn.classList.remove("enabled");

});
