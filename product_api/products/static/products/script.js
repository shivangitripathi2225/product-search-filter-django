let currentPage = 1;

// Fetch products from API
async function fetchProducts() {
    const search = document.getElementById("search").value;
    const category = document.getElementById("category").value;
    const sort = document.getElementById("sort").value;

    // Build query params
    let url = `/products?page=${currentPage}`;

    if (search) url += `&search=${search}`;
    if (category) url += `&category=${category}`;
    if (sort) url += `&sort=${sort}`;

    try {
        const response = await fetch(url);
        const data = await response.json();

        renderProducts(data.products);
    } catch (error) {
        console.error("Error fetching products:", error);
    }
}

// Render products to UI
function renderProducts(products) {
    const container = document.getElementById("product-list");
    container.innerHTML = "";

    if (products.length === 0) {
        container.innerHTML = "<p>No products found</p>";
        return;
    }

    products.forEach(product => {
        const div = document.createElement("div");
        div.innerHTML = `
            <h3>${product.name}</h3>
            <p>Category: ${product.category}</p>
            <p>Price: ₹${product.price}</p>
            <hr/>
        `;
        container.appendChild(div);
    });
}

// Event listeners
document.getElementById("search").addEventListener("input", () => {
    currentPage = 1;
    fetchProducts();
});

document.getElementById("category").addEventListener("change", () => {
    currentPage = 1;
    fetchProducts();
});

document.getElementById("sort").addEventListener("change", () => {
    currentPage = 1;
    fetchProducts();
});

// Pagination
document.getElementById("prev").addEventListener("click", () => {
    if (currentPage > 1) {
        currentPage--;
        fetchProducts();
    }
});

document.getElementById("next").addEventListener("click", () => {
    currentPage++;
    fetchProducts();
});

// Initial load
fetchProducts();