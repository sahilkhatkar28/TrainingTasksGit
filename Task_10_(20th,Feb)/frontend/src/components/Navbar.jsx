import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="bg-gray-900 p-4 text-white flex justify-between">
      <Link to="/" className="text-xl font-bold">E-Commerce</Link>
      <div>
        <Link to="/products" className="mx-3">Products</Link>
        <Link to="/cart" className="mx-3">Cart</Link>
      </div>
    </nav>
  );
}
