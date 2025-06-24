async function fetchDirectLink() {
  const ytLink = document.getElementById("yt-link").value;
  const output = document.getElementById("output");

  output.innerHTML = "⏳ Wird verarbeitet...";

  try {
    const response = await fetch("/get_link", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ url: ytLink })
    });

    const data = await response.json();
    if (data.error) {
      output.innerHTML = `<span style="color: red;">❌ Fehler: ${data.error}</span>`;
    } else {
      output.innerHTML = `✅ <strong>Direktlink:</strong> <a href="${data.direct_url}" target="_blank">${data.direct_url}</a>`;
    }
  } catch (err) {
    output.innerHTML = `<span style="color: red;">❌ Verbindung fehlgeschlagen</span>`;
  }
}

