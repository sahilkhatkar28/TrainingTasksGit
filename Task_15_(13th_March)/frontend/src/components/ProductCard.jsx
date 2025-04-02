const ProductCard = ({ product }) => {
    return (
        <div className="border p-4 rounded-lg shadow-md bg-white">
            <h2 className="text-lg font-semibold">{product.name}</h2>
            <p className="text-gray-600">Category: {product.category}</p>
            <p className="text-gray-800 font-bold">${product.price}</p>
        </div>
    );
};

export default ProductCard;
