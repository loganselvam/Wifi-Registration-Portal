-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 07, 2023 at 05:47 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `python_wifi_portal`
--

-- --------------------------------------------------------

--
-- Table structure for table `staff_register`
--

CREATE TABLE `staff_register` (
  `id` int(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `staff_register`
--

INSERT INTO `staff_register` (`id`, `email`, `gender`, `password`) VALUES
(1, 'guru@gmail.com', 'male', '123');

-- --------------------------------------------------------

--
-- Table structure for table `staff_wifi_details`
--

CREATE TABLE `staff_wifi_details` (
  `id` int(10) NOT NULL,
  `register_no` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `depart` varchar(50) NOT NULL,
  `contact` varchar(50) NOT NULL,
  `device` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `mac` varchar(50) NOT NULL,
  `designation` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `staff_wifi_details`
--

INSERT INTO `staff_wifi_details` (`id`, `register_no`, `name`, `depart`, `contact`, `device`, `email`, `date`, `mac`, `designation`) VALUES
(1, '7498484', 'guru', 'dme', '789454654', 'dev', 'guruextazee@gmail.com', '2023-03-16', 'mac', 'des');

-- --------------------------------------------------------

--
-- Table structure for table `student_wifi_details`
--

CREATE TABLE `student_wifi_details` (
  `id` int(10) NOT NULL,
  `register_no` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `depart` varchar(50) NOT NULL,
  `contact` varchar(50) NOT NULL,
  `device` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `mac` varchar(50) NOT NULL,
  `hostel` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_wifi_details`
--

INSERT INTO `student_wifi_details` (`id`, `register_no`, `name`, `depart`, `contact`, `device`, `email`, `date`, `mac`, `hostel`) VALUES
(1, '17508395', 'guru', 'dme', '78945455445', 'fjskjedfs', 'vimal@gmail.com', '2023-03-24', 'dfsdfs', 'yes');

-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

CREATE TABLE `user_details` (
  `id` int(10) NOT NULL,
  `register_no` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_details`
--

INSERT INTO `user_details` (`id`, `register_no`, `email`, `gender`, `password`) VALUES
(1, '17508395', 'guru@gmail.com', 'male', '123');
