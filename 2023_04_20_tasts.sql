-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 24, 2023 at 12:17 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `2023.04.20_tasts`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `Customer_ID` int(6) NOT NULL,
  `Customer_First_Name` varchar(30) CHARACTER SET utf8 COLLATE utf8_latvian_ci NOT NULL,
  `Customer_Last_Name` varchar(30) CHARACTER SET utf8 COLLATE utf8_latvian_ci NOT NULL,
  `Customer_Phone` varchar(20) CHARACTER SET utf8 COLLATE utf8_latvian_ci NOT NULL,
  `Customer _Email` varchar(50) CHARACTER SET utf8 COLLATE utf8_latvian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`Customer_ID`, `Customer_First_Name`, `Customer_Last_Name`, `Customer_Phone`, `Customer _Email`) VALUES
(0, 'Marta', 'Mistere', '+37129196870', 'marta.mistere@gmail.com'),
(1, 'Janis', 'Berzins', '+371 20001100', 'janis.berzins@gmail,com'),
(2, 'Gatis', 'Kauss', '+37129257015', 'gatis.kauss@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `Order_ID` int(6) NOT NULL,
  `Total_amount` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_latvian_ci NOT NULL,
  `Order_date` date NOT NULL,
  `Order_status` varchar(30) CHARACTER SET utf8 COLLATE utf8_latvian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`Order_ID`, `Total_amount`, `Order_date`, `Order_status`) VALUES
(42001, '1', '2023-04-20', 'Done'),
(42002, '5', '2023-04-20', 'Canceled'),
(42301, '2', '2023-04-23', 'In processing');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `Product_ID` varchar(6) CHARACTER SET utf8 COLLATE utf8_latvian_ci NOT NULL,
  `Quantity` varchar(3) CHARACTER SET utf8 COLLATE utf8_latvian_ci DEFAULT NULL,
  `Product_type` text CHARACTER SET utf8 COLLATE utf8_latvian_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`Product_ID`, `Quantity`, `Product_type`) VALUES
('000333', '7', 'Apple MacBook Pro'),
('000222', '8', 'Lenova IdeaPad'),
('000111', '3', 'Lenova ThinkBook'),
('000222', '8', NULL),
('000111', '3', 'Lenova ThinkBook');

-- --------------------------------------------------------

--
-- Table structure for table `suppliers`
--

CREATE TABLE `suppliers` (
  `Suppliers_ID` int(6) DEFAULT NULL,
  `Suppliers_Company_Name` varchar(30) CHARACTER SET utf8 COLLATE utf8_latvian_ci NOT NULL,
  `Suppliers_First_Name` varchar(30) CHARACTER SET utf8 COLLATE utf8_latvian_ci NOT NULL,
  `Suppliers_Last_Name` varchar(30) CHARACTER SET utf8 COLLATE utf8_latvian_ci NOT NULL,
  `Suppliers_Phone` varchar(30) CHARACTER SET utf8 COLLATE utf8_latvian_ci NOT NULL,
  `Suppliers_Email` varchar(50) CHARACTER SET utf8 COLLATE utf8_latvian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `suppliers`
--

INSERT INTO `suppliers` (`Suppliers_ID`, `Suppliers_Company_Name`, `Suppliers_First_Name`, `Suppliers_Last_Name`, `Suppliers_Phone`, `Suppliers_Email`) VALUES
(5, 'Apple', 'Jone', 'Peak', '+370893848585', 'Jone.peak@gmail.com'),
(6, 'Lenova', 'Santa', 'Romano', '+371 234567879', 'santa.romano@gmail.com'),
(7, 'ASUS', 'Genrihs', 'Pesh', '+371 2344556978', 'genrihs.pesh@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`Customer_ID`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`Order_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `Order_ID` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42302;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
