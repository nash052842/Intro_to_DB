SELECT 
    BOOK_NAME,
    BOOK_AUTHOR, 
    BOOK_orders, 
    BOOK_customers,
     COLUMN_DEFAULT,
    EXTRA
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_SCHEMA = 'alx_book_store'
    AND TABLE_NAME = 'Books';
