Name:           ros-kinetic-pr2-navigation-self-filter
Version:        0.1.28
Release:        0%{?dist}
Summary:        ROS pr2_navigation_self_filter package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_navigation_self_filter
Source0:        %{name}-%{version}.tar.gz

Requires:       assimp
Requires:       bullet-devel
Requires:       ros-kinetic-filters
Requires:       ros-kinetic-pcl-ros
Requires:       ros-kinetic-resource-retriever
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-urdf
Requires:       ros-kinetic-visualization-msgs
BuildRequires:  assimp-devel
BuildRequires:  bullet-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-filters
BuildRequires:  ros-kinetic-pcl-ros
BuildRequires:  ros-kinetic-resource-retriever
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-urdf
BuildRequires:  ros-kinetic-visualization-msgs

%description
Filters the robot's body out of point clouds.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Apr 27 2018 David Feil-Seifer <dave@cse.unr.edu> - 0.1.28-0
- Autogenerated by Bloom

* Thu Apr 12 2018 Devon Ash <dash@clearpathrobotics.com> - 0.1.27-0
- Autogenerated by Bloom

