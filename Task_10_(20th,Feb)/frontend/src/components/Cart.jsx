import { useQuery, useMutation } from "react-query";
import { getCart, checkout, removeFromCart } from "../api/cart";

export default function Cart() {
  const { data: cartItems = [], isLoading, isError, refetch } = useQuery("cart", getCart);
  const removeItemMutation = useMutation(removeFromCart, {
    onSuccess: () => refetch(),
  });

  const handleCheckout = async () => {
    try {
      await checkout();
      alert("Order placed!");
      refetch();
    } catch (error) {
      alert("Checkout failed! Please try again.");
    }
  };

  const handleRemove = async (itemId) => {
    try {
      await removeItemMutation.mutateAsync(itemId);
    } catch (error) {
      alert("Failed to remove item.");
    }
  };

  if (isLoading) return <p>Loading cart...</p>;
  if (isError) return <p>Failed to load cart. Please try again.</p>;

  return (
    <div className="p-4">
      <h2 className="text-2xl font-semibold mb-4">Cart</h2>
      {cartItems.length > 0 ? (
        cartItems.map((item) => (
          <div key={item.id} className="border p-2 my-2 flex justify-between items-center">
            <div>
              <p>Product ID: {item.product_id}</p>
              <p>Quantity: {item.quantity}</p>
            </div>
            <button
              onClick={() => handleRemove(item.id)}
              className="bg-red-500 text-white px-2 py-1 rounded"
            >
              Remove
            </button>
          </div>
        ))
      ) : (
        <p>Your cart is empty.</p>
      )}
      {cartItems.length > 0 && (
        <button onClick={handleCheckout} className="mt-4 bg-green-500 text-white px-4 py-2 rounded">
          Checkout
        </button>
      )}
    </div>
  );
}
