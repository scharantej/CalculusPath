## Flask Application Design for "Build a Website that Creates a Learning Path to Master Calculus"

### HTML Files

- **index.html**: This will be the main landing page for the application. It will provide an overview of the purpose of the application and the various learning resources available.
- **learning-path.html**: This page will present the learning path to master calculus. It will include a breakdown of topics, recommended resources, and interactive exercises.
- **resources.html**: This page will provide a curated list of external resources relevant to calculus, such as online courses, videos, and textbooks.

### Routes

**@app.route('/')**
- Function: Directs users to the main landing page (index.html).

**@app.route('/learning-path')**
- Function: Displays the learning path to master calculus (learning-path.html).

**@app.route('/resources')**
- Function: Lists external resources related to calculus (resources.html).

**@app.route('/progress-tracker')**
- Function: Allows users to track their progress through the learning path (not implemented in this design but could be added for future functionality).

**@app.route('/exercises')**
- Function: Provides interactive exercises related to calculus topics (not implemented in this design but could be added for future functionality).

**@app.route('/about')**
- Function: Displays information about the application and its creators (e.g., contact information, version history).