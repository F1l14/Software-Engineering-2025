-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 22, 2025 at 05:07 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `LinQ-SEProject`
--

-- --------------------------------------------------------

--
-- Table structure for table `business`
--

CREATE TABLE `business` (
  `name` varchar(80) NOT NULL,
  `owner` varchar(80) NOT NULL,
  `logo` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `departments`
--

CREATE TABLE `departments` (
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `departments`
--

INSERT INTO `departments` (`name`) VALUES
('Ανθρώπινο Δυναμικό'),
('Διοίκηση'),
('Έρευνα και Ανάπτυξη'),
('Λογιστήριο'),
('Μάρκετινγκ'),
('Νομικό Τμήμα'),
('Πληροφορική'),
('Προμήθειες'),
('Πωλήσεις'),
('Υποστήριξη');

-- --------------------------------------------------------

--
-- Table structure for table `department_notices`
--

CREATE TABLE `department_notices` (
  `notice_id` int(11) NOT NULL,
  `department` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `username` varchar(80) NOT NULL,
  `department` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employees`
--

INSERT INTO `employees` (`username`, `department`) VALUES
('anikolaou', 'Πωλήσεις'),
('epanagiotou', 'Ανθρώπινο Δυναμικό'),
('gpapadopoulos', 'Πληροφορική'),
('ivasileiou', 'Προμήθειες'),
('kchatzidaki', 'Νομικό Τμήμα'),
('kdimetriou', 'Μάρκετινγκ'),
('mkonstantinou', 'Λογιστήριο'),
('nstathopoulos', 'Έρευνα και Ανάπτυξη'),
('santoniou', 'Διοίκηση'),
('tmichailidis', 'Υποστήριξη');

-- --------------------------------------------------------

--
-- Table structure for table `employee_tags`
--

CREATE TABLE `employee_tags` (
  `employee` varchar(80) NOT NULL,
  `tag` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `events`
--

CREATE TABLE `events` (
  `id` int(11) NOT NULL,
  `notice_id` int(11) NOT NULL,
  `start` datetime NOT NULL,
  `end` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `managers`
--

CREATE TABLE `managers` (
  `username` varchar(80) NOT NULL,
  `department` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `managers`
--

INSERT INTO `managers` (`username`, `department`) VALUES
('epanagiotou', 'Ανθρώπινο Δυναμικό'),
('kdimetriou', 'Μάρκετινγκ'),
('santoniou', 'Διοίκηση');

-- --------------------------------------------------------

--
-- Table structure for table `messages`
--

CREATE TABLE `messages` (
  `id` int(11) NOT NULL,
  `history_id` int(11) NOT NULL,
  `from_user` varchar(80) NOT NULL,
  `to_user` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `messages_history`
--

CREATE TABLE `messages_history` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL,
  `user_1` varchar(80) NOT NULL,
  `user_2` varchar(80) NOT NULL,
  `history` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`history`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `notices`
--

CREATE TABLE `notices` (
  `id` int(11) NOT NULL,
  `type` enum('business','department','team') NOT NULL,
  `created` timestamp NOT NULL DEFAULT current_timestamp(),
  `body` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `notifications`
--

CREATE TABLE `notifications` (
  `id` int(11) NOT NULL,
  `user` varchar(80) NOT NULL,
  `type` enum('placeholder') NOT NULL,
  `body` text NOT NULL,
  `created` timestamp NOT NULL DEFAULT current_timestamp(),
  `opened` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `projects`
--

CREATE TABLE `projects` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL,
  `description` text NOT NULL,
  `team_id` int(11) DEFAULT NULL,
  `created` timestamp NOT NULL DEFAULT current_timestamp(),
  `status` enum('unassigned','assigned','completed') NOT NULL DEFAULT 'unassigned',
  `completed_at` datetime DEFAULT NULL,
  `deadline` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `projects`
--

INSERT INTO `projects` (`id`, `name`, `description`, `team_id`, `created`, `status`, `completed_at`, `deadline`) VALUES
(1, 'ERP Εφαρμογή', 'Ανάπτυξη συστήματος ERP για την εταιρεία', 1, '2025-05-22 13:14:27', 'completed', '2025-05-22 16:33:48', '2025-07-15 00:00:00'),
(2, 'Web Portal Πελατών', 'Δημιουργία διαδραστικού portal για πελάτες', 3, '2025-05-22 13:14:27', 'completed', '2025-05-22 16:33:55', '2025-06-20 00:00:00'),
(3, 'Σύστημα HR', 'Διαχείριση προσωπικού και αιτήσεων', NULL, '2025-05-22 13:14:27', 'unassigned', NULL, '2025-09-30 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `project_departments`
--

CREATE TABLE `project_departments` (
  `project_id` INT NOT NULL,
  `department_name` varchar(80) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `project_departments`
--

INSERT INTO `project_departments` (`project_id`, `department_name`) VALUES
('2', 'Διοίκηση'),
('1', 'Διοίκηση'),
('2', 'Πληροφορική');

-- --------------------------------------------------------

--
-- Table structure for table `project_tags`
--

CREATE TABLE `project_tags` (
  `project` varchar(80) NOT NULL,
  `tag` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `project_tags`
--

INSERT INTO `project_tags` (`project`, `tag`) VALUES
('ERP Εφαρμογή', 'backend'),
('Web Portal Πελατών', 'frontend'),
('Σύστημα HR', 'urgent');

-- --------------------------------------------------------

--
-- Table structure for table `tags`
--

CREATE TABLE `tags` (
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tags`
--

INSERT INTO `tags` (`name`) VALUES
('backend'),
('documentation'),
('frontend'),
('high-priority'),
('urgent');

-- --------------------------------------------------------

--
-- Table structure for table `tasks`
--

CREATE TABLE `tasks` (
  `id` int(11) NOT NULL,
  `team_id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL,
  `assigned_to` varchar(80) NOT NULL,
  `state` enum('pending','completed') NOT NULL DEFAULT 'pending'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `teams`
--

CREATE TABLE `teams` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL,
  `department` varchar(80) NOT NULL,
  `leader` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `teams`
--

INSERT INTO `teams` (`id`, `name`, `department`, `leader`) VALUES
(1, 'Ομάδα Ανάπτυξης ERP', 'Έρευνα και Ανάπτυξη', 'nstathopoulos'),
(2, 'Ομάδα HR', 'Ανθρώπινο Δυναμικό', 'epanagiotou'),
(3, 'Ομάδα Portal Πελατών', 'Πωλήσεις', 'anikolaou');

-- --------------------------------------------------------

--
-- Table structure for table `team_members`
--

CREATE TABLE `team_members` (
  `team_id` int(11) NOT NULL,
  `member` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `team_members`
--

INSERT INTO `team_members` (`team_id`, `member`) VALUES
(1, 'gpapadopoulos'),
(1, 'nstathopoulos'),
(2, 'epanagiotou'),
(3, 'kdimetriou'),
(3, 'mkonstantinou');

-- --------------------------------------------------------

--
-- Table structure for table `team_notices`
--

CREATE TABLE `team_notices` (
  `notice_id` int(11) NOT NULL,
  `team_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `username` varchar(80) NOT NULL,
  `password` varchar(80) NOT NULL,
  `position` varchar(80) NOT NULL,
  `firstname` varchar(80) NOT NULL,
  `lastname` varchar(80) NOT NULL,
  `email` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`username`, `password`, `firstname`, `lastname`) VALUES
('admin', 'root', 'Αναστάσιος', 'Παπαδόπουλος'),
('anikolaou', 'root', 'Αντώνης', 'Νικολάου'),
('epanagiotou', 'root', 'Ελένη', 'Παναγιώτου'),
('gpapadopoulos', 'root', 'Γιάννης', 'Παπαδόπουλος'),
('ivasileiou', 'root', 'Ιωάννα', 'Βασιλείου'),
('kchatzidaki', 'root', 'Κατερίνα', 'Χατζηδάκη'),
('kdimetriou', 'root', 'Κώστας', 'Δημητρίου'),
('mkonstantinou', 'root', 'Μαρία', 'Κωνσταντίνου'),
('nstathopoulos', 'root', 'Νίκος', 'Σταθόπουλος'),
('santoniou', 'root', 'Σοφία', 'Αντωνίου'),
('tmichailidis', 'root', 'Θανάσης', 'Μιχαηλίδης');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `business`
--
ALTER TABLE `business`
  ADD PRIMARY KEY (`name`),
  ADD KEY `business_owner_user` (`owner`);

--
-- Indexes for table `departments`
--
ALTER TABLE `departments`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `department_notices`
--
ALTER TABLE `department_notices`
  ADD PRIMARY KEY (`notice_id`,`department`),
  ADD KEY `dep_notice_depname` (`department`);

--
-- Indexes for table `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`username`,`department`),
  ADD KEY `employee_department_name` (`department`);

--
-- Indexes for table `employee_tags`
--
ALTER TABLE `employee_tags`
  ADD PRIMARY KEY (`employee`,`tag`),
  ADD KEY `employee_tags_tag` (`tag`);

--
-- Indexes for table `events`
--
ALTER TABLE `events`
  ADD PRIMARY KEY (`id`,`notice_id`),
  ADD KEY `event_notice_id` (`notice_id`);

--
-- Indexes for table `managers`
--
ALTER TABLE `managers`
  ADD PRIMARY KEY (`username`,`department`),
  ADD KEY `manager_department_name` (`department`);

--
-- Indexes for table `messages`
--
ALTER TABLE `messages`
  ADD PRIMARY KEY (`id`),
  ADD KEY `message_history_id` (`history_id`),
  ADD KEY `message_from_user` (`from_user`),
  ADD KEY `message_to_user` (`to_user`);

--
-- Indexes for table `messages_history`
--
ALTER TABLE `messages_history`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `notices`
--
ALTER TABLE `notices`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `notifications`
--
ALTER TABLE `notifications`
  ADD PRIMARY KEY (`id`),
  ADD KEY `notification_user` (`user`);

--
-- Indexes for table `projects`
--
ALTER TABLE `projects`
  ADD PRIMARY KEY (`id`),
  ADD KEY `project_team_id` (`team_id`);

--
-- Indexes for table `projects`
--
ALTER TABLE `project_departments`
  ADD PRIMARY KEY (`project_id, department_name`);

--
-- Indexes for table `project_tags`
--
ALTER TABLE `project_tags`
  ADD PRIMARY KEY (`project`,`tag`),
  ADD KEY `project_tags_tag` (`tag`);

--
-- Indexes for table `tags`
--
ALTER TABLE `tags`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `tasks`
--
ALTER TABLE `tasks`
  ADD PRIMARY KEY (`id`,`team_id`),
  ADD KEY `task_team_id` (`team_id`),
  ADD KEY `task_assigned_member` (`assigned_to`);

--
-- Indexes for table `teams`
--
ALTER TABLE `teams`
  ADD PRIMARY KEY (`id`),
  ADD KEY `team_leader_employee` (`leader`),
  ADD KEY `team_department` (`department`);

--
-- Indexes for table `team_members`
--
ALTER TABLE `team_members`
  ADD PRIMARY KEY (`team_id`,`member`),
  ADD KEY `member_employee` (`member`);

--
-- Indexes for table `team_notices`
--
ALTER TABLE `team_notices`
  ADD PRIMARY KEY (`notice_id`,`team_id`),
  ADD KEY `team_notice_teamid` (`team_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `events`
--
ALTER TABLE `events`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `messages`
--
ALTER TABLE `messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `messages_history`
--
ALTER TABLE `messages_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `notices`
--
ALTER TABLE `notices`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `notifications`
--
ALTER TABLE `notifications`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `projects`
--
ALTER TABLE `projects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tasks`
--
ALTER TABLE `tasks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `teams`
--
ALTER TABLE `teams`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `business`
--
ALTER TABLE `business`
  ADD CONSTRAINT `business_owner_user` FOREIGN KEY (`owner`) REFERENCES `users` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `department_notices`
--
ALTER TABLE `department_notices`
  ADD CONSTRAINT `dep_notice_depname` FOREIGN KEY (`department`) REFERENCES `departments` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `dep_notice_id` FOREIGN KEY (`notice_id`) REFERENCES `notices` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `employees`
--
ALTER TABLE `employees`
  ADD CONSTRAINT `employee_department_name` FOREIGN KEY (`department`) REFERENCES `departments` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `employee_user_username` FOREIGN KEY (`username`) REFERENCES `users` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `employee_tags`
--
ALTER TABLE `employee_tags`
  ADD CONSTRAINT `employee_tags_employee` FOREIGN KEY (`employee`) REFERENCES `employees` (`username`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `employee_tags_tag` FOREIGN KEY (`tag`) REFERENCES `tags` (`name`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `events`
--
ALTER TABLE `events`
  ADD CONSTRAINT `event_notice_id` FOREIGN KEY (`notice_id`) REFERENCES `notices` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `managers`
--
ALTER TABLE `managers`
  ADD CONSTRAINT `manager_department_name` FOREIGN KEY (`department`) REFERENCES `departments` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `manager_user_username` FOREIGN KEY (`username`) REFERENCES `users` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `messages`
--
ALTER TABLE `messages`
  ADD CONSTRAINT `message_from_user` FOREIGN KEY (`from_user`) REFERENCES `users` (`username`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `message_history_id` FOREIGN KEY (`history_id`) REFERENCES `messages_history` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `message_to_user` FOREIGN KEY (`to_user`) REFERENCES `users` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `notifications`
--
ALTER TABLE `notifications`
  ADD CONSTRAINT `notification_user` FOREIGN KEY (`user`) REFERENCES `users` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `projects`
--
ALTER TABLE `projects`
  ADD CONSTRAINT `project_team_id` FOREIGN KEY (`team_id`) REFERENCES `teams` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
  ADD CONSTRAINT `depart` FOREIGN KEY (`departments`) REFERENCES `departments` (`name`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `projects`
--
ALTER TABLE `project_departments`
  ADD CONSTRAINT `project_id` FOREIGN KEY (`project_id`) REFERENCES `projects`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
  ADD CONSTRAINT `department_name` FOREIGN KEY (`department_name`) REFERENCES `departments`(`name`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `project_tags`
--
ALTER TABLE `project_tags`
  ADD CONSTRAINT `project_tags_tag` FOREIGN KEY (`tag`) REFERENCES `tags` (`name`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tasks`
--
ALTER TABLE `tasks`
  ADD CONSTRAINT `task_assigned_member` FOREIGN KEY (`assigned_to`) REFERENCES `team_members` (`member`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `task_team_id` FOREIGN KEY (`team_id`) REFERENCES `teams` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `teams`
--
ALTER TABLE `teams`
  ADD CONSTRAINT `team_department` FOREIGN KEY (`department`) REFERENCES `departments` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `team_leader_employee` FOREIGN KEY (`leader`) REFERENCES `employees` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `team_members`
--
ALTER TABLE `team_members`
  ADD CONSTRAINT `member_employee` FOREIGN KEY (`member`) REFERENCES `employees` (`username`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `members_team_id` FOREIGN KEY (`team_id`) REFERENCES `teams` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `team_notices`
--
ALTER TABLE `team_notices`
  ADD CONSTRAINT `team_notice_id` FOREIGN KEY (`notice_id`) REFERENCES `notices` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `team_notice_teamid` FOREIGN KEY (`team_id`) REFERENCES `teams` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
