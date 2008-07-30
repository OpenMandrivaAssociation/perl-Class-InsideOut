%define module   Class-InsideOut

Name:		perl-%{module}
Version:    1.09
Release:    %mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
Summary:    DISTSUMMARY
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Class/%{module}-%{version}.tar.gz
BuildRequires: perl-devel
BuildRequires: perl(Class::ISA)
BuildRequires: perl(Config)
BuildRequires: perl(Exporter)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(base)
BuildArch: noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
DISTDESCR

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL -n INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/Class
