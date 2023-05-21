window.onload = function() {
    let searchInput = document.getElementById('searchInput');
    const toggleBtn = document.querySelector(".sidebar-toggle");
    const closeBtn = document.querySelector(".close-btn");
    const sidebar = document.querySelector(".sidebar");

    toggleBtn.addEventListener("click", function () {
        sidebar.classList.toggle("show-sidebar");
    });

    closeBtn.addEventListener("click", function () {
        sidebar.classList.remove("show-sidebar");
    });
    searchInput.addEventListener('keyup', function(e) {
        let searchQuery = e.target.value.toLowerCase();

        let questionBlocks = document.getElementsByClassName('question-block');
        for (let i = 0; i < questionBlocks.length; i++) {
            let questionText = questionBlocks[i].getElementsByTagName('h2')[0].innerText;
            if (questionText.toLowerCase().indexOf(searchQuery) > -1) {
                questionBlocks[i].style.transition = "all 0.5s";
                questionBlocks[i].style.opacity = "1";
                questionBlocks[i].style.maxHeight = "1000px";
            } else {
                questionBlocks[i].style.transition = "all 0.5s";
                questionBlocks[i].style.opacity = "0";
                questionBlocks[i].style.maxHeight = "0";
            }
        }

        let answerBlocks = document.getElementsByClassName('answer-block');
        for (let i = 0; i < answerBlocks.length; i++) {
            let answerText = answerBlocks[i].getElementsByTagName('h2')[0].innerText;
            if (answerText.toLowerCase().indexOf(searchQuery) > -1) {
                answerBlocks[i].style.transition = "all 0.5s";
                answerBlocks[i].style.opacity = "1";
                answerBlocks[i].style.maxHeight = "1000px";
            } else {
                answerBlocks[i].style.transition = "all 0.5s";
                answerBlocks[i].style.opacity = "0";
                answerBlocks[i].style.maxHeight = "0";
            }
        }

    });
}
