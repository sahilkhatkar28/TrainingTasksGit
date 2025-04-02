import { addToCart } from "../api/cart";

export default function ProductCard({ product }) {
  const handleAddToCart = async () => {
    await addToCart(product.id, 1);
    alert("Added to cart!");
  };

  return (
    <div className="border p-4 rounded-lg shadow-md">
      <h2 className="text-lg font-semibold">{product.name}</h2>
      <p className="text-gray-600">${product.price}</p>
      <button onClick={handleAddToCart} className="mt-2 bg-blue-500 text-white px-4 py-2 rounded">
        Add to Cart
      </button>
    </div>
  );
}
