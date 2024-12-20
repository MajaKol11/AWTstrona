document.addEventListener("DOMContentLoaded", () => {
    const daysGrid = document.getElementById("daysGrid");
    const dayDetails = document.getElementById("dayDetails");
    const selectedDaySpan = document.getElementById("selectedDay");
    const submitBtn = document.getElementById("submitBtn");
    const confirmationMessage = document.getElementById("confirmationMessage");

    // Generate days for the calendar (example: 30 days)
    for (let i = 1; i <= 30; i++) {
        const dayBtn = document.createElement("button");
        dayBtn.textContent = `Day ${i}`;
        dayBtn.addEventListener("click", () => {
            selectedDaySpan.textContent = `Day ${i}`;
            dayDetails.classList.remove("hidden");
        });
        daysGrid.appendChild(dayBtn);
    }

    // Handle send request button click
	submitBtn.addEventListener("click", () => {
		console.log("Removing 'hidden' class from confirmationMessage");
		confirmationMessage.classList.remove("hidden");
		confirmationMessage.style.display = "block";

		setTimeout(() => {
			confirmationMessage.style.display = "none";
		}, 3000);
	});





	if (submitBtn) 
	{
		submitBtn.addEventListener("click", () => {
            console.log("Submit button was clicked!");
        });
    } 
	else 
	{
        console.log("Submit button not found!");
    }

	
});
