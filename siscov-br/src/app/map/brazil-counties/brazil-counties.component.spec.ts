import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BrazilCountiesComponent } from './brazil-counties.component';

describe('BrazilCountiesComponent', () => {
  let component: BrazilCountiesComponent;
  let fixture: ComponentFixture<BrazilCountiesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BrazilCountiesComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BrazilCountiesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
