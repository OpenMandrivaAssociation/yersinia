%define	name	yersinia
%define	version 0.7.1
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Network pen-testing tool
License: 	GPL
Group: 		System/Servers
Source:		http://www.yersinia.net/download/%{name}-%{version}.tar.bz2
Url: 		http://www.yersinia.net
BuildRequires:	libnet1.1.2-devel
BuildRequires:	ncurses-devel
BuildRequires:  libpcap-devel
BuildRequires:  pkgconfig
BuildRequires:  gtk2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Yersinia is a network tool designed to take advantage of some weakeness in
different network protocols. It pretends to be a solid framework for analyzing
and testing the deployed networks and systems.

Currently, only attacks for the following network protocols are implemented:
* Spanning Tree Protocol (STP).
* Cisco Discovery Protocol (CDP).
* Dynamic Trunking Protocol (DTP).
* Dynamic Host Configuration Protocol (DHCP).
* Hot Standby Router Protocol (HSRP).
* 802.1q.
* Inter-Switch Link Protocol (ISL).
* VLAN Trunking Protocol (VTP).

%prep
%setup -q

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog FAQ INSTALL README THANKS TODO
%{_bindir}/*
%{_mandir}/man8/*

