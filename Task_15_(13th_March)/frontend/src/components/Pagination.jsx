const Pagination = ({ currentPage, totalPages, onPageChange }) => {
    return (
        <div className="flex justify-center space-x-2 mt-4">
            <button 
                className="px-4 py-2 bg-gray-300 rounded" 
                disabled={currentPage === 1} 
                onClick={() => onPageChange(currentPage - 1)}>
                Previous
            </button>
            <span className="px-4 py-2">{currentPage} / {totalPages}</span>
            <button 
                className="px-4 py-2 bg-gray-300 rounded" 
                disabled={currentPage === totalPages} 
                onClick={() => onPageChange(currentPage + 1)}>
                Next
            </button>
        </div>
    );
};

export default Pagination;
