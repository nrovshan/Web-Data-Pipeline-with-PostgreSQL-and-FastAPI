Create table if not exists books (
                   id serial primary key,
                   title text,
                   price text,
                   stars text,
                   stock text,
                   category text,
                   book_tax text,
                   number_reviews text,
                   page_url text,
                   loaded_at timestamp);
    