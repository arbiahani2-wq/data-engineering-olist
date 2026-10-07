# Olist Data Model

## orders

- Grain : 1 ligne = 1 commande 
- Primary Key: `order_id`
- Foreign Key: `customer_id` → `customers.customer_id`

## customers

- Grain: 1 ligne = 1 enregistrement client
- Primary Key: `customer_id`


## order_items

- Grain: 1 ligne = 1 article d'une commande
- Primary Key: `order_id` + `order_item_id`
- Foreign Keys:
  - `order_id` → `orders.order_id`
  - `product_id` → `products.product_id`
  - `seller_id` → `sellers.seller_id`

## order_payments

- Grain: 1 ligne = 1 paiement associé à une commande
- Foreign Key: `order_id` → `orders.order_id`

## order_reviews

- Grain: 1 ligne = 1 avis associé à une commande
- Foreign Key: `order_id` → `orders.order_id`

## products

- Grain: 1 ligne = 1 produit
- Primary Key: `product_id`

## sellers

- Grain: 1 ligne = 1 vendeur
- Primary Key: `seller_id`

## geolocation

- Grain: 1 ligne = 1 enregistrement géographique
- Primary Key: à déterminer

## translations

- Grain: 1 ligne = 1 catégorie produit
- Primary Key: `product_category_name`

