<template>
  <Chart :options="chartOptions"/>
</template>

<script>
import {Chart} from 'highcharts-vue'

export default {
  name: 'TimesheetChart',
  components: {Chart},
  props: {
    employees: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      chartOptions: {
        chart: {
          type: 'column',
          backgroundColor: 'transparent',

        },
        title: {
          text: 'Employee Total Hours Worked',
          align: 'left'
        },
        subtitle: {
          text: "",
          align: 'left'
        },
        xAxis: {
          categories: this.employees.map((employee) => {
            return employee.name
          }),
          crosshair: true,
          accessibility: {
            description: 'Countries'
          }
        },
        yAxis: {
          min: 0,
          title: {
            text: 'Hours (H)'
          }
        },
        tooltip: {
          valueSuffix: 'Hours (H)'
        },
        plotOptions: {
          column: {
            pointPadding: 0.2,
            borderWidth: 0
          }
        },
        series: this.employees.map((employee) => {
          return {
            name: employee.name,
            data: [employee.totalHours]
          }
        }),
      }
    }
  },
  computed: {
    employeesWorkedHours() {
      return this.employees.map((employee) => {
        return {
          name: employee.name,
          totalHours: employee.totalHours,
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
