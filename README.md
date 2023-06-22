# __inventory-management__

## __About__
The inventory management system is a web-based application that incorporates __Django’s__ authentication middleware for authenticating incoming request by validating session and authenticates them respectively through forms using the user models. Further, decorators and mixins are used to restrict the access the views and URLs based on the authentication. 
The system uses HTML and CSS through Django’s templates to display user with forms and details of inventory along with their purchases and sales. It is designed to track and manage inventory items efficiently by making purchases and sales from/to various companies using their GST number and store them in the inventory model. Each of these operations are done through different URLs and are managed by the views.
