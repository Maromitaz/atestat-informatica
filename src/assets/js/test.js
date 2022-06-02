let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 44.4875, lng: 26.1165 },
    zoom: 18,
  });
}
