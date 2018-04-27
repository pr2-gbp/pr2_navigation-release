Name:           ros-indigo-pr2-navigation-teleop
Version:        0.1.28
Release:        0%{?dist}
Summary:        ROS pr2_navigation_teleop package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_navigation_teleop
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-pr2-machine
Requires:       ros-indigo-pr2-teleop
Requires:       ros-indigo-topic-tools
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-pr2-machine
BuildRequires:  ros-indigo-pr2-teleop
BuildRequires:  ros-indigo-topic-tools

%description
This package holds a special teleop configuration for the PR2 robot that should
be used when running applications that use autonomous navigation.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Apr 27 2018 David Feil-Seifer <dave@cse.unr.edu> - 0.1.28-0
- Autogenerated by Bloom

* Mon Jun 22 2015 Devon Ash <dash@clearpathrobotics.com> - 0.1.27-0
- Autogenerated by Bloom

* Tue Feb 10 2015 Devon Ash <dash@clearpathrobotics.com> - 0.1.26-0
- Autogenerated by Bloom

* Fri Feb 06 2015 Devon Ash <dash@clearpathrobotics.com> - 0.1.25-0
- Autogenerated by Bloom

