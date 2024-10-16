// File: static/script.js
const quizQuestions = [
    { question: "What is the capital of France?", options: ["Paris", "Rome", "Madrid", "Berlin"], answer: "Paris" },
    { question: "Which planet is known as the Red Planet?", options: ["Mars", "Jupiter", "Venus", "Saturn"], answer: "Mars" },
    // Add 8 more questions
];

function loadQuiz() {
    const quizContainer = document.getElementById('quiz-container');
    quizQuestions.forEach((q, index) => {
        let quizHtml = `<p>${index + 1}. ${q.question}</p>`;
        q.options.forEach(option => {
            quizHtml += `<input type="radio" name="question${index}" value="${option}"> ${option} <br>`;
        });
        quizContainer.innerHTML += quizHtml;
    });
}

function submitQuiz() {
    let score = 0;
    quizQuestions.forEach((q, index) => {
        const selectedOption = document.querySelector(`input[name="question${index}"]:checked`);
        if (selectedOption && selectedOption.value === q.answer) {
            score++;
        }
    });
    fetch('/submit-quiz', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ score: score }),
    }).then(response => response.json()).then(data => {
        window.location.href = "/leaderboard";
    });
}

window.onload = loadQuiz;



// File: static/script.js

function submitQuiz() {
    const form = document.getElementById('quiz-form');
    const formData = new FormData(form);

    fetch('/submit_quiz', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        alert('Quiz submitted successfully!');
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


