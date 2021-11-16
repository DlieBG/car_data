import { Component, OnInit } from '@angular/core';
import { interval, Observable } from 'rxjs';
import { switchMap } from 'rxjs/operators';
import { DashboardService } from './dashboard.service';
import { OBD } from './dashboard.type';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {

  obd$!: Observable<OBD>;

  constructor(private dashboardService: DashboardService) { }

  ngOnInit(): void {
    this.getOBD();
  }

  getOBD() {
    this.obd$ = interval(1000).pipe(switchMap(() => this.dashboardService.getOBD()));
  }

  getGear(rpm: number, speed: number): string {
    if (speed < 1) {
      return "-";
    }
    const ratio = rpm / speed;
    if (120 < ratio) {
      return "1";
    }
    if (69 < ratio && ratio < 75) {
      return "2";
    }
    if (47 < ratio && ratio < 51) {
      return "3";
    }
    if (34 < ratio && ratio < 37) {
      return "4";
    }
    if (27 < ratio && ratio < 30) {
      return "5";
    }
    return "-";
  }

}
