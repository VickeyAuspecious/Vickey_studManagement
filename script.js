document.getElementById('add-student').addEventListener('click', function() {
    var studentName = document.getElementById('student-name').value;
    var age = document.getElementById('age').value;
    var address = document.getElementById('address').value;
    var mobile = document.getElementById('mobile').value;
    var fatherName = document.getElementById('fatherName').value;
    var motherName = document.getElementById('motherName').value;
    var department = document.getElementById('department').value;

    if (studentName.trim() === '' || age.trim() === '' || address.trim() === '' || mobile.trim() === '' || fatherName.trim() === '' || motherName.trim() === '' || department.trim() === '') {
        alert('Please fill in all the fields.');
        return;
    }

    var studentList = document.getElementById('student-list');
    var studentItem = document.createElement('div');
    studentItem.className = 'student-item';
    studentItem.innerHTML = '<strong>' + studentName + '</strong><br>' +
                            'Age: ' + age + '<br>' +
                            'Address: ' + address + '<br>' +
                            'Mobile: ' + mobile + '<br>' +
                            'Father\'s Name: ' + fatherName + '<br>' +
                            'Mother\'s Name: ' + motherName + '<br>' +
                            'Department: ' + department;
    studentList.appendChild(studentItem);

    document.getElementById('student-name').value = '';
    document.getElementById('age').value = '';
    document.getElementById('address').value = '';
    document.getElementById('mobile').value = '';
    document.getElementById('fatherName').value = '';
    document.getElementById('motherName').value = '';
    document.getElementById('department').value = '';
});