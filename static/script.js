document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("seatContainer");
  if (container) {
    for (let i = 1; i <= 50; i++) {
      const seat = document.createElement("div");
      seat.classList.add("seat");
      seat.textContent = i;
      seat.addEventListener("click", () => seat.classList.toggle("selected"));
      container.appendChild(seat);
    }
  }
});

function submitSeats() {
  const selectedSeats = Array.from(document.querySelectorAll(".seat.selected")).map(s => s.textContent);
  if (selectedSeats.length === 0) {
    alert("Please select at least one seat!");
    return false;
  }
  document.getElementById("selectedSeatsInput").value = selectedSeats.join(", ");
  return true;
}
