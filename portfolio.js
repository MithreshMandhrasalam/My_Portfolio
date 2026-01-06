<script>
    const tabs = document.querySelectorAll(".tab");
    const contents = document.querySelectorAll(".skills-content");

    tabs.forEach(tab => {
        tab.addEventListener("click", () => {
            tabs.forEach(t => t.classList.remove("active"));
            contents.forEach(c => c.classList.remove("show"));

            tab.classList.add("active");
            document.getElementById(tab.dataset.target).classList.add("show");
        });
    });
</script>