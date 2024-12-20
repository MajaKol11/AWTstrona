    function validateForm() {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        if (!username || !password) {
            alert('Please fill in both the username and password fields.');
            return false;
        }
        return true;
    }