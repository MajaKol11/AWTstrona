function checkForm() {
	const name = document.getElementById('name').value.trim();
	const email = document.getElementById('email').value.trim();
	const password = document.getElementById('password').value.trim();
	const phone = document.getElementById('phone').value.trim();
	const username = document.getElementById('username').value.trim();

	//Check if any field is empty
	if (!name || !email || !password || !phone || !username) {
		alert('Please fill out all fields before signing up.');
		return;
	}

	//Submit form if all fields are filled
	document.getElementById('signup-form').submit();
}