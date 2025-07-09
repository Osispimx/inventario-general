const passwordInput = document.getElementsByClassName('password');
const togglePasswordButton = document.getElementById('togglePassword');

togglePasswordButton.addEventListener('click', function () {
    const currentType = passwordInput[0].type;
    passwordInput[0].type = currentType === 'password' ? 'text' : 'password';
    togglePasswordButton.innerHTML = currentType === 'password' 
        ? '<i class="fas fa-eye"></i>'  // Ojo abierto
        : '<i class="fas fa-eye-slash"></i>';  // Ojo cerrado
});