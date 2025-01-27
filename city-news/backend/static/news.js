const newsContainer = document.getElementById("news-container");
const API_HOST = "/api"; // Relative path to API

let currentPage = 1;
let perPage = 5;

function renderNews(news) {
    newsContainer.innerHTML = ""; // Clear existing news
    news.forEach((item) => {
        const newsItem = document.createElement("div");
        newsItem.className = "news-item";
        newsItem.textContent = item;
        newsContainer.appendChild(newsItem);
    });
}

async function fetchNews(page = 1, perPage = 5) {
    try {
        const response = await fetch(`${API_HOST}/news?page=${page}&per_page=${perPage}`); // Use relative path
        const data = await response.json();
        renderNews(data);
        updatePaginationControls(data.length);
    } catch (error) {
        console.error("Error fetching news:", error);
    }
}

function nextPage() {
    currentPage++;
    fetchNews(currentPage, perPage);
}

function previousPage() {
    if (currentPage > 1) {
        currentPage--;
        fetchNews(currentPage, perPage);
    }
}

function updatePaginationControls(newsLength) {
    const previousButton = document.getElementById("previous-button");
    const nextButton = document.getElementById("next-button");

    previousButton.style.display = currentPage > 1 ? "inline-block" : "none";
    nextButton.style.display = newsLength === perPage ? "inline-block" : "none";
}

function updatePerPage(event) {
    perPage = parseInt(event.target.value);
    currentPage = 1;
    fetchNews(currentPage, perPage);
}

document.addEventListener("DOMContentLoaded", () => {
    fetchNews();
    document.getElementById("next-button").addEventListener("click", nextPage);
    document.getElementById("previous-button").addEventListener("click", previousPage);
    document.getElementById("per-page-select").addEventListener("change", updatePerPage);
});
