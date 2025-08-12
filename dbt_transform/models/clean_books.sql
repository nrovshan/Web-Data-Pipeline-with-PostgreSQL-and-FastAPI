{{ config(materialized = 'table') }}


with source as (
    select * from public.books
),

cleaned as (
    select 
         id,
         title,
         cast(substring(price from 2) as numeric) as price,
         substring(price from 1 for 1) as currency,
         case 
            when stars = 'One' then 1
            when stars = 'Two' then 2
            when stars = 'Three' then 3
            when stars = 'Four' then 4
            when stars = 'Five' then 5 
            else null
            end as star_rating,
            stock,
            category,
            book_tax,
            number_reviews,
            page_url,
            loaded_at
    from source
)

select * from cleaned