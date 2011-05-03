Summary:	Network pen-testing tool
Name:		yersinia
Version:	0.7.2
Release:	%mkrel 0.20060323.3
License: 	GPL
Group: 		System/Servers
Source:		http://www.yersinia.net/download/%{name}-snapshot.tgz
URL: 		http://www.yersinia.net
BuildRequires:	gtk2-devel
BuildRequires:	net-devel >= 1.1.3
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	pcap-devel
BuildRequires:	pkgconfig
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%setup -q -n %{name}

%build
make distclean
rm -f configure
sh ./autogen.sh

%configure2_5x \
    --with-pcap-includes=%{_includedir}/pcap

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
