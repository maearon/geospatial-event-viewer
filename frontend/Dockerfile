# Image chính thức của Node.js
FROM node:18

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy package.json và lock file trước để cache được layer npm install
COPY package*.json ./

# Cài đặt các package
RUN npm install

# Copy toàn bộ mã nguồn vào image
COPY . .

# Mặc định chạy Vite dev server (hot reload)
CMD ["npm", "run", "dev", "--", "--host"]
