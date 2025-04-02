import { useEffect, useState } from "react";
import { getProducts } from "../api/api";
import ProductCard from "../components/ProductCard";
import Pagination from "../components/Pagination";

const Products = () => {
    const [products, setProducts] = useState([]);
    const [page, setPage] = useState(1);
    const [totalPages, setTotalPages] = useState(1);
    const [category, setCategory] = useState("");
    const [search, setSearch] = useState("");

    useEffect(() => {
        fetchProducts();
    }, [page, category, search]);

    const fetchProducts = async () => {
        const data = await getProducts(page, 5, category, search);
        setProducts(data.products);
        setTotalPages(data.pages);
    };

    return (
        <div className="container mx-auto p-6">
            <h1 className="text-2xl font-bold mb-4">Product List</h1>

            <div className="flex space-x-4 mb-4">
                <input 
                    type="text" 
                    placeholder="Search..." 
                    className="border p-2 rounded w-1/3"
                    value={search} 
                    onChange={(e) => setSearch(e.target.value)} 
                />
                <select 
                    className="border p-2 rounded" 
                    value={category} 
                    onChange={(e) => setCategory(e.target.value)}
                >
                    <option value="">All Categories</option>
                    <option value="electronics">Electronics</option>
                    <option value="fashion">Fashion</option>
                    <option value="home">Home</option>
                </select>
            </div>

            <div className="grid grid-cols-3 gap-4">
                {products.map((product) => (
                    <ProductCard key={product.id} product={product} />
                ))}
            </div>

            <Pagination currentPage={page} totalPages={totalPages} onPageChange={setPage} />
        </div>
    );
};

export default Products;
