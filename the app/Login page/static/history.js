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

        let qaBlocks = document.getElementsByClassName('qa-block');
        for (let i = 0; i < qaBlocks.length; i++) {
            let qaText = qaBlocks[i].innerText;
            if (searchQuery !== "" && qaText.toLowerCase().indexOf(searchQuery) === -1) {
                qaBlocks[i].style.transition = "all 0.5s";
                qaBlocks[i].style.opacity = "0";
                qaBlocks[i].style.maxHeight = "0";
            } else {
                qaBlocks[i].style.transition = "all 0.5s";
                qaBlocks[i].style.opacity = "1";
                qaBlocks[i].style.maxHeight = "1000px";
            }
        }
    });
}
