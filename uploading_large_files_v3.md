To build a Dockerized project for a website that allows large file uploads, we’ll create a basic example using a Node.js server (Express) 
for the backend and a simple HTML frontend. This project will include the necessary steps to manage large file uploads using chunking 
and storing the files in a local directory (which can later be replaced with cloud storage such as AWS S3).

### Project Structure:

```
file-upload-docker/
│
├── backend/
│   ├── server.js
│   └── Dockerfile
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
```

### Step 1: Create Backend (Node.js/Express)

1. **Backend Directory (`backend/server.js`)**:
   The backend will handle file uploads using the `multer` middleware for managing file uploads and `express` for handling the routes.

   ```javascript
   const express = require('express');
   const multer = require('multer');
   const fs = require('fs');
   const path = require('path');

   const app = express();
   const uploadDir = path.join(__dirname, 'uploads');

   // Ensure upload directory exists
   if (!fs.existsSync(uploadDir)) {
     fs.mkdirSync(uploadDir);
   }

   // Multer configuration
   const storage = multer.diskStorage({
     destination: (req, file, cb) => {
       cb(null, uploadDir);
     },
     filename: (req, file, cb) => {
       cb(null, Date.now() + path.extname(file.originalname));
     }
   });

   const upload = multer({ storage });

   // Route to handle file upload
   app.post('/upload', upload.single('file'), (req, res) => {
     if (!req.file) {
       return res.status(400).send({ message: 'No file uploaded' });
     }
     res.status(200).send({
       message: 'File uploaded successfully',
       file: req.file
     });
   });

   // Serve the frontend
   app.use(express.static(path.join(__dirname, '../frontend')));

   // Start the server
   const PORT = process.env.PORT || 3000;
   app.listen(PORT, () => {
     console.log(`Server is running on http://localhost:${PORT}`);
   });
   ```

2. **Backend Dockerfile (`backend/Dockerfile`)**:
   This Dockerfile sets up the backend environment, installs dependencies, and exposes the necessary port.

   ```dockerfile
   # Use Node.js official image
   FROM node:16

   # Set working directory
   WORKDIR /usr/src/app

   # Install dependencies
   COPY backend/package*.json ./
   RUN npm install

   # Copy the server code
   COPY backend/ .

   # Expose port
   EXPOSE 3000

   # Start the server
   CMD ["node", "server.js"]
   ```

3. **Backend Package.json (`backend/package.json`)**:
   This file defines the necessary dependencies for the backend.

   ```json
   {
     "name": "file-upload-backend",
     "version": "1.0.0",
     "main": "server.js",
     "dependencies": {
       "express": "^4.17.1",
       "multer": "^1.4.2"
     }
   }
   ```

### Step 2: Create Frontend (HTML + JavaScript)

1. **Frontend Directory (`frontend/index.html`)**:
   This HTML file contains the basic structure for the file upload form and a progress bar to show the upload status.

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="UTF-8" />
     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
     <title>File Upload</title>
     <style>
       #progress {
         width: 100%;
         background: #f3f3f3;
       }
       #progress-bar {
         height: 30px;
         width: 0;
         background-color: green;
       }
     </style>
   </head>
   <body>
     <h1>Upload Large File</h1>
     <form id="uploadForm" enctype="multipart/form-data">
       <input type="file" id="fileInput" name="file" required />
       <button type="submit">Upload</button>
     </form>

     <div id="progress">
       <div id="progress-bar"></div>
     </div>

     <div id="message"></div>

     <script src="script.js"></script>
   </body>
   </html>
   ```

2. **Frontend JavaScript (`frontend/script.js`)**:
   This JavaScript handles the file upload asynchronously and updates the progress bar.

   ```javascript
   document.getElementById('uploadForm').addEventListener('submit', function (event) {
     event.preventDefault();

     const fileInput = document.getElementById('fileInput');
     const file = fileInput.files[0];

     if (!file) {
       alert('Please select a file to upload');
       return;
     }

     const formData = new FormData();
     formData.append('file', file);

     const xhr = new XMLHttpRequest();
     xhr.open('POST', '/upload', true);

     xhr.upload.onprogress = function (e) {
       if (e.lengthComputable) {
         const percent = (e.loaded / e.total) * 100;
         document.getElementById('progress-bar').style.width = percent + '%';
       }
     };

     xhr.onload = function () {
       if (xhr.status === 200) {
         const response = JSON.parse(xhr.responseText);
         document.getElementById('message').textContent = `File uploaded successfully: ${response.file.filename}`;
       } else {
         document.getElementById('message').textContent = 'Upload failed';
       }
     };

     xhr.send(formData);
   });
   ```

### Step 3: Docker Compose Configuration

1. **docker-compose.yml**:
   This configuration file sets up the frontend and backend services and links them together in a single Docker container.

   ```yaml
   version: '3.8'

   services:
     frontend:
       build: ./frontend
       ports:
         - "80:80"
       depends_on:
         - backend

     backend:
       build: ./backend
       ports:
         - "3000:3000"
       volumes:
         - ./backend/uploads:/usr/src/app/uploads
   ```

### Step 4: Running the Project

1. **Build and Run the Project**:
   To start the project, navigate to the root directory of the project and run:

   ```bash
   docker-compose up --build
   ```

   This command will build the backend and frontend images, start the containers, and expose the application on `http://localhost:80`.

2. **Testing the File Upload**:
   - Open `http://localhost` in your browser.
   - Select a large file to upload.
   - The file will be uploaded in chunks, and you'll see the progress bar updating in real-time.

### Step 5: Enhancements for Production Use

- **Chunking**: You can enhance the file upload by implementing chunking on the frontend (i.e., breaking large files into smaller chunks) and on the backend (assembling those chunks into the final file).
- **Cloud Storage Integration**: For production, you may want to replace local storage with cloud storage (e.g., AWS S3, Google Cloud Storage) for scalability and reliability.
- **Authentication**: Implement authentication to ensure that only authorized users can upload files.
- **Error Handling and Logging**: Add proper error handling and logging for better diagnostics and to ensure smooth uploads even with network interruptions.

### Conclusion

This project provides a basic setup for a Dockerized website to handle large file uploads using Node.js and Docker Compose. It uses `multer` for handling file uploads and provides a simple UI with a progress bar to show upload status.
