-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 27, 2020 at 08:15 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `database`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `course_code` varchar(25) NOT NULL,
  `roll_no` varchar(25) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`course_code`, `roll_no`, `date`, `status`) VALUES
('2cs301', '12bee0123', '2020-04-27', 'PRESENT'),
('2cs401', '12bee0123', '2020-04-27', 'PRESENT'),
('2cs402', '12bee0123', '2020-04-27', 'PRESENT'),
('2cs402', '13bee231', '2020-04-27', 'PRESENT'),
('2cs402', '13bee0123', '2020-04-27', 'PRESENT'),
('2cs402', '12bee0123', '2020-04-27', 'ABSENT'),
('2cs402', '13bee231', '2020-04-27', 'PRESENT'),
('2cs402', '13bee0123', '2020-04-27', 'PRESENT'),
('2cs402', '12bee0123', '2020-04-27', 'ABSENT'),
('2cs402', '13bee231', '2020-04-27', 'ABSENT'),
('2cs402', '13bee0123', '2020-04-27', 'PRESENT'),
('2cs301', '12bee0123', '2020-04-27', 'ABSENT'),
('2cs301', '12bee0123', '2020-04-27', 'ABSENT'),
('2cs301', '12bee0123', '2020-04-27', 'ABSENT'),
('2cs301', '12bee0123', '2020-04-27', 'PRESENT'),
('2cs301', '12bee0123', '2020-04-27', 'ABSENT'),
('2cs301', '12bee0123', '2020-04-27', 'PRESENT'),
('2cs402', '12bee0123', '2020-04-27', 'PRESENT'),
('2cs402', '13bee231', '2020-04-27', 'ABSENT'),
('2cs402', '13bee0123', '2020-04-27', 'ABSENT'),
('2cs402', '12bee0123', '2020-04-27', 'PRESENT'),
('2cs402', '13bee231', '2020-04-27', 'ABSENT'),
('2cs402', '13bee453', '2020-04-27', 'ABSENT'),
('2cs402', '13bee0123', '2020-04-27', 'PRESENT'),
('2cs401', '12bee0123', '2020-04-27', 'ABSENT'),
('2cs402', '12bee0123', '2020-04-27', 'PRESENT'),
('2cs402', '13bee231', '2020-04-27', 'PRESENT'),
('2cs402', '13bee453', '2020-04-27', 'ABSENT'),
('2cs402', '13bee0123', '2020-04-27', 'PRESENT'),
('2cs402', '12bee0123', '2020-04-27', 'PRESENT'),
('2cs402', '13bee231', '2020-04-27', 'ABSENT'),
('2cs402', '13bee453', '2020-04-27', 'PRESENT'),
('2cs402', '13bee0123', '2020-04-27', 'ABSENT'),
('2cs301', '12bee0123', '2020-04-27', 'PRESENT');

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `course_code` varchar(25) NOT NULL,
  `course_name` varchar(25) NOT NULL,
  `sem` int(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`course_code`, `course_name`, `sem`) VALUES
('2cs301', 'DSA', 3),
('2cs302', 'OOP', 3),
('2cs303', 'DE', 3),
('2cs304', 'DM', 3),
('2cs401', 'CA', 4),
('2cs402', 'PSC', 4),
('2cs403', 'OS', 4),
('2cs404', 'DBMS', 4),
('2cs405', 'PS', 4);

-- --------------------------------------------------------

--
-- Table structure for table `faculty`
--

CREATE TABLE `faculty` (
  `fid` int(25) NOT NULL,
  `name` varchar(25) NOT NULL,
  `email` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `faculty`
--

INSERT INTO `faculty` (`fid`, `name`, `email`, `password`) VALUES
(1, 'as ma\'am', 'S@nirmauni.ac.in', 'dbms'),
(2, 'ae ma\'am', 'a@nirmauni.ac.in', 'psc'),
(3, 'hs sir', 'd@nirmauni.ac.in', 'psc'),
(4, '', '', ''),
(9, 'noone', '13bee453@nirmauni.ac.in', 'noone');

-- --------------------------------------------------------

--
-- Table structure for table `record`
--

CREATE TABLE `record` (
  `fid` int(25) NOT NULL,
  `roll_no` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `sample`
--

CREATE TABLE `sample` (
  `name` varchar(25) NOT NULL,
  `roll_no` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sample`
--

INSERT INTO `sample` (`name`, `roll_no`) VALUES
('trump', '12bee0123'),
('somone', '13bee231'),
('noone', '13bee453'),
('asd', '13bee0123');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `sid` int(25) NOT NULL,
  `name` varchar(25) NOT NULL,
  `roll_no` varchar(25) NOT NULL,
  `email` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `section` int(25) NOT NULL,
  `year` int(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`sid`, `name`, `roll_no`, `email`, `password`, `section`, `year`) VALUES
(1, 'asd', '13bee0123', '13bee0123@nirmauni.ac.in', 'asd', 1, 2020),
(2, 'somone', '13bee231', '13bee231@nirmauni.ac.in', 'bala', 1, 2020),
(3, 'trump', '12bee0123', '12bee0123@nirmauni.ac.in', 'trump', 1, 2020),
(4, '', '', '', '', 0, 0),
(9, 'noone', '13bee453', '13bee453@nirmauni.ac.in', 'noone', 1, 2020);

-- --------------------------------------------------------

--
-- Table structure for table `takes`
--

CREATE TABLE `takes` (
  `roll_no` varchar(25) NOT NULL,
  `course_code` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `takes`
--

INSERT INTO `takes` (`roll_no`, `course_code`) VALUES
('12bee0123', '2cs301'),
('12bee0123', '2cs302'),
('12bee0123', '2cs303'),
('12bee0123', '2cs304'),
('12bee0123', '2cs401'),
('12bee0123', '2cs402'),
('12bee0123', '2cs403'),
('12bee0123', '2cs404'),
('12bee0123', '2cs405'),
('13bee231', '2cs301'),
('13bee231', '2cs302'),
('13bee231', '2cs303'),
('13bee231', '2cs402'),
('13bee231', '2cs404'),
('13bee453', '2cs301'),
('13bee453', '2cs302'),
('13bee453', '2cs303'),
('13bee453', '2cs402'),
('13bee453', '2cs404'),
('13bee0123', '2cs304'),
('13bee0123', '2cs401'),
('13bee0123', '2cs402'),
('13bee0123', '2cs403'),
('13bee0123', '2cs405');

-- --------------------------------------------------------

--
-- Table structure for table `teaches`
--

CREATE TABLE `teaches` (
  `fid` int(25) NOT NULL,
  `fname` varchar(25) NOT NULL,
  `course_code` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `teaches`
--

INSERT INTO `teaches` (`fid`, `fname`, `course_code`, `password`) VALUES
(0, 'pimal ma\'am'', '2cs401', '2cs401'),
(0, 'rajesh sir', '2cs301', '2cs301'),
(0, 'as ma\'am'', '2cs404', '2cs401'),
(0, 'ae ma\'am'', '2cs302', '2cs401'),
(0, 'noone', '2cs402', '2cs40123'),
(0, 'sir', '2cs301', '2cs301');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `uid` int(20) NOT NULL,
  `email` varchar(25) NOT NULL,
  `name` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendance`
--
ALTER TABLE `attendance`
  ADD KEY `course_code` (`course_code`);

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`course_code`);

--
-- Indexes for table `faculty`
--
ALTER TABLE `faculty`
  ADD PRIMARY KEY (`fid`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `record`
--
ALTER TABLE `record`
  ADD PRIMARY KEY (`fid`,`roll_no`);

--
-- Indexes for table `sample`
--
ALTER TABLE `sample`
  ADD UNIQUE KEY `roll_no` (`roll_no`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`sid`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `takes`
--
ALTER TABLE `takes`
  ADD PRIMARY KEY (`roll_no`,`course_code`);

--
-- Indexes for table `teaches`
--
ALTER TABLE `teaches`
  ADD PRIMARY KEY (`fname`,`course_code`),
  ADD KEY `course_code` (`course_code`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`uid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `faculty`
--
ALTER TABLE `faculty`
  MODIFY `fid` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `sid` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `uid` int(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `attendance`
--
ALTER TABLE `attendance`
  ADD CONSTRAINT `attendance_ibfk_1` FOREIGN KEY (`course_code`) REFERENCES `course` (`course_code`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `teaches`
--
ALTER TABLE `teaches`
  ADD CONSTRAINT `teaches_ibfk_1` FOREIGN KEY (`course_code`) REFERENCES `course` (`course_code`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
