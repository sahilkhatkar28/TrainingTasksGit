import { useQuery } from "react-query";
import { getProducts } from "../api/products";
import ProductCard from "../components/ProductCard";

export default function Products() {
  const { data: products } = useQuery("products", getProducts);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-semibold mb-4">Products</h1>
      <div className="grid grid-cols-3 gap-4">
        {products?.map((product) => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </div>
  );
}
