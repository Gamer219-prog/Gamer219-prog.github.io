async function fetchDirectLink() {
  const ytLink = document.getElementById("yt-link").value;
  const output = document.getElementById("output");

  const response = await fetch("/get_link", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ url: ytLink })
  });

  const data = await response.json();
  if (data.error) {
    output.textContent = "Fehler: " + data.error;
  } else {
    output.innerHTML = `GoogleVideo-Link: <a href="${data.direct_url}" target="_blank">Ansehen</a>`;
  }
}
