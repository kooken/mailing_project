# Mailing Management Service

This project is a Django-based service designed to manage and administer mailing campaigns, offering comprehensive functionality for CRUD operations, user management, and analytics.

### Key Features:
1. **Mailing Management**: 
   - Create, view, edit, and delete mailing campaigns.
   - Schedule mailings to run periodically using `apscheduler`.
   - Detailed statistics for each mailing, including delivery attempts and server responses.
   
2. **Client Management**: 
   - Manage the clients who receive mailings through a dedicated CRUD interface.
   - Each mailing is linked to a single message and multiple clients.
   
3. **User Roles & Access Control**:
   - Custom user model with email registration and verification using `AbstractUser`.
   - Role-based access control (admin, manager, and regular users), ensuring proper permission settings.
   - Managers can view mailings and users but cannot modify campaigns.
   
4. **Blog Module**:
   - Integrated blog for content promotion, featuring CRUD for articles, and tracking views.
   - Displays random blog articles on the home page.
   
5. **Statistics Dashboard**:
   - Overview of the number of mailings, active campaigns, and unique clients.
   - Home page displaying key metrics and blog posts.

6. **Caching**:
   - Cached content for blog posts and home page metrics to optimize performance.

### Technical Stack:
- **Django Forms** for non-admin interfaces.
- **Fixture support** for database seeding (mailings, messages, clients, user roles, and blog).
- **Scheduled Tasks** handled via `apscheduler`.
- **Bootstrap** for the user interface.

This project is designed to streamline client engagement through periodic mailings, while ensuring flexibility, scalability, and ease of use for administrators.
