const quiz = [
    ["What is Superman's real name?","Clark Kent"],
    ["What is Wonder Woman's real name?","Diana Prince"],
    ["What is Batman's real name?","Bruce Wayne"]
];
let score = 0;// initialize score


for(const [question,answer] of quiz){ //loops through and gets keys:values and saves as variables
    const response = prompt(question); //the answer given to the question is saved as response
    if(response === answer){
        alert('Correct!');
        score++;
    } else {
        alert(`Wrong! The correct answer was ${answer}`);
    }
    }

// At the end of the game, report the player's score
alert(`Game Over, you scored ${score} point${score !== 1 ? 's' : ''}`); // if score isnt 1 use 's' otherwise use empty string
