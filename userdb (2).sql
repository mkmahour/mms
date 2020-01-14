-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 15, 2019 at 08:41 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `userdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id_medition` int(10) NOT NULL,
  `medition_name` varchar(100) NOT NULL,
  `compny_name` varchar(100) NOT NULL,
  `mfd` date NOT NULL,
  `exp_d` date NOT NULL,
  `quantity` int(10) NOT NULL,
  `price` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id_medition`, `medition_name`, `compny_name`, `mfd`, `exp_d`, `quantity`, `price`) VALUES
(5, 'nisu gold', 'horizon', '2019-10-11', '2021-10-11', 100, 1),
(6, 'nisu gold', 'horizon', '2019-11-10', '2021-11-21', 100, 1),
(14, 'alprex', 'genric', '2019-12-30', '2021-12-30', 100, 2),
(15, 'combiflaim', 'test', '2019-05-05', '2020-05-05', 6, 15);

-- --------------------------------------------------------

--
-- Table structure for table `admin_login`
--

CREATE TABLE `admin_login` (
  `login_id` varchar(10) NOT NULL,
  `password` varchar(10) NOT NULL,
  `nick_name` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin_login`
--

INSERT INTO `admin_login` (`login_id`, `password`, `nick_name`) VALUES
('mk@gmail.c', '123', 'mk');

-- --------------------------------------------------------

--
-- Table structure for table `itom`
--

CREATE TABLE `itom` (
  `s.n.` int(10) NOT NULL,
  `itom_name` varchar(40) NOT NULL,
  `quantity` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `itom`
--

INSERT INTO `itom` (`s.n.`, `itom_name`, `quantity`) VALUES
(68, 'flip cold', 2);

-- --------------------------------------------------------

--
-- Table structure for table `treeview`
--

CREATE TABLE `treeview` (
  `medition_name` varchar(20) NOT NULL,
  `compny_name` varchar(20) NOT NULL,
  `mfd` varchar(20) NOT NULL,
  `exp_d` varchar(20) NOT NULL,
  `quantity` int(10) NOT NULL,
  `price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `treeview`
--

INSERT INTO `treeview` (`medition_name`, `compny_name`, `mfd`, `exp_d`, `quantity`, `price`) VALUES
('combiflaim', 'cruewell', '2019-10-18', '2021-05-01', 4, 4),
('combiflaim', 'cruewell', '2019-10-18', '2021-05-01', 300, 300);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id_medition`);

--
-- Indexes for table `itom`
--
ALTER TABLE `itom`
  ADD PRIMARY KEY (`itom_name`),
  ADD UNIQUE KEY `s.n.` (`s.n.`,`itom_name`,`quantity`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id_medition` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `itom`
--
ALTER TABLE `itom`
  MODIFY `s.n.` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
