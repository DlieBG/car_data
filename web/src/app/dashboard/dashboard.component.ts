import { Component, OnInit } from '@angular/core';
import { CronJob } from 'cron';
import { Observable } from 'rxjs';
import { DashboardService } from './dashboard.service';
import { OBD } from './dashboard.type';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {

  obd!: OBD;
  obd$!: Observable<OBD>;

  constructor(private dashboardService: DashboardService) { }

  ngOnInit(): void {
    new CronJob('* * * * * *', () => {
      this.getOBD();
    }).start();

    this.getOBD();
  }

  getOBD() {
    this.obd$ = this.dashboardService.getOBD();
    this.obd$.subscribe(obd => this.obd = obd);
  }

}
