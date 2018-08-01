const quiz = [
    ["What is Superman's real name?","Clark Kent"],
    ["What is Wonder Woman's real name?","Diana Prince"],
    ["What is Batman's real name?","Bruce Wayne"]
];


function start(quiz){
    let score = 0;

    //main game loop
    for (const [question, answer] of quiz){ //loops through and gets keys:values and saves as variables
        const response =ask(question); //the answer given to the question is saved as response
        check(response,answer);
    }

    // end of main game loop

    gameOver();

    // function declarations
    function ask(question){
        return prompt(question);
    }

    function check(response,answer){
        if(response === answer){
        alert('Correct!');
        score++;
        } else {
        alert(`Wrong! The correct answer was ${answer}`);
        }
    }

    function gameOver(){ // At the end of the game, report the player's score
        alert(`Game Over, you scored ${score} point${score !== 1 ? 's' : ''}`);
    }
}

start(quiz);


/*
The ask(), check() and gameOver() functions are defined at the end of the body of the start() function. 
They need to be placed inside the start() function as nested functions, as this gives them access to any variables defined inside the start() function's scope. 
Because they are defined using function declarations, they are hoisted, so they can be defined after they are invoked.
*/
