window.addEventListener("load", function () {
  if (!("geolocation" in navigator)) {
    console.log("Browser geolocation support illa.");
    return;
  }

  const latInput = document.getElementById("id_current_lat");
  const lngInput = document.getElementById("id_current_lng");

  if (!latInput || !lngInput) {
    console.log("Lat/Lng inputs not found in admin form.");
    return;
  }

  navigator.geolocation.getCurrentPosition(
    function (pos) {
      latInput.value = pos.coords.latitude.toFixed(6);
      lngInput.value = pos.coords.longitude.toFixed(6);
    },
    function (err) {
      console.log("Geo error:", err);
      alert("error :does not read: " + err.message);
    },
    { enableHighAccuracy: true }
  );
});
