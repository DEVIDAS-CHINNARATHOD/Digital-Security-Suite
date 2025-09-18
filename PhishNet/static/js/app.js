async function checkURL() {
  const url = document.getElementById("urlInput").value;
  const res = await fetch("/check_url", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url })
  });
  const data = await res.json();
  document.getElementById("urlResult").innerText =
    `Status: ${data.status}, Score: ${data.score}, Reasons: ${data.reasons.join(", ")}`;
}

async function checkInsta() {
  const username = document.getElementById("instaInput").value;
  const res = await fetch("/check_insta", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username })
  });
  const data = await res.json();
  document.getElementById("instaResult").innerText =
    `Status: ${data.status}, Score: ${data.score}, Reasons: ${data.reasons.join(", ")}`;
}

async function checkAPK() {
  const filename = document.getElementById("apkInput").value;
  const res = await fetch("/check_apk", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ filename })
  });
  const data = await res.json();
  document.getElementById("apkResult").innerText =
    `Status: ${data.status}, Score: ${data.score}, Reasons: ${data.reasons.join(", ")}`;
}
